import gradio as gr
import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor, XGBClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

global_df = {}

def upload_file(file):
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        df = pd.read_csv(file.name)
    elif ext == 'json':
        df = pd.read_json(file.name)
    else:
        return "Unsupported format", None

    # Save in memory for later steps
    global_df['df'] = df
    return "✅ File uploaded!", df.head()

def clean_data(method):
    df = global_df.get('df')
    if df is None:
        return "❌ Upload file first!", None

    if method == "Drop missing rows":
        df_clean = df.dropna()
    elif method == "Fill with 0":
        df_clean = df.fillna(0)
    elif method == "Fill with mean":
        df_clean = df.fillna(df.mean(numeric_only=True))
    global_df['df'] = df_clean
    return "✅ Cleaned!", df_clean.head()

def plot_heatmap():
    df = global_df.get('df')
    if df is None:
        return "❌ Upload file first!", None

    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    return fig

def run_xgboost(target, model_type):
    df = global_df.get('df')
    if df is None:
        return "❌ Upload file first!", None

    try:
        X = df.drop(columns=[target]).dropna()
        y = df[target].dropna()

        X = pd.get_dummies(X, drop_first=True)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        if model_type == "Regression":
            model = XGBRegressor()
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            score = mean_squared_error(y_test, preds, squared=False)
            result = f"✅ RMSE: {score:.2f}"
        else:
            model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            score = accuracy_score(y_test, preds)
            result = f"✅ Accuracy: {score * 100:.2f}%"
        return result, pd.DataFrame({"Actual": y_test[:10].values, "Predicted": preds[:10]})
    except Exception as e:
        return f"❌ Error: {e}", None

with gr.Blocks() as demo:
    gr.Markdown("# 📊 CSV Analyzer with Gradio")

    with gr.Tab("Upload"):
        file_input = gr.File(label="Upload CSV or JSON")
        upload_btn = gr.Button("Upload & Preview")
        upload_output = gr.Textbox()
        upload_df = gr.Dataframe()

    upload_btn.click(upload_file, inputs=file_input, outputs=[upload_output, upload_df])

    with gr.Tab("Clean Data"):
        clean_method = gr.Radio(["Drop missing rows", "Fill with 0", "Fill with mean"])
        clean_btn = gr.Button("Clean")
        clean_output = gr.Textbox()
        clean_df = gr.Dataframe()

    clean_btn.click(clean_data, inputs=clean_method, outputs=[clean_output, clean_df])

    with gr.Tab("Heatmap"):
        heatmap_btn = gr.Button("Generate Heatmap")
        heatmap_output = gr.Plot()

    heatmap_btn.click(plot_heatmap, outputs=heatmap_output)

    with gr.Tab("XGBoost"):
        target_col = gr.Textbox(label="Target Column Name")
        model_type = gr.Radio(["Regression", "Classification"])
        xgb_btn = gr.Button("Run XGBoost")
        xgb_output = gr.Textbox()
        xgb_df = gr.Dataframe()

    xgb_btn.click(run_xgboost, inputs=[target_col, model_type], outputs=[xgb_output, xgb_df])

demo.launch()
