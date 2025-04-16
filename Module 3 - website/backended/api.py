from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ 支持前端跨域访问
from model_code import match_houses

app = Flask(__name__)
CORS(app)  # ✅ 启用 CORS

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    query = data.get("query", "")

    try:
        # ✅ 获取推荐结果
        df = match_houses(query)

        # ✅ 如果为空或 None，直接返回空列表，避免 .head() 报错
        if df is None or df.empty:
            print("❌ match_houses returned None or empty dataframe")
            return jsonify({"results": []})

        # ✅ 安全地输出调试信息
        print("✅ df from match_houses:\n", df.head())
        print("📋 df columns:", df.columns.tolist())

        # ✅ 构建安全的返回内容
        try:
            if all(col in df.columns for col in ["ADDRESS", "RENT_PRICE"]):
                results = df[["ADDRESS", "RENT_PRICE"]].fillna("N/A").to_dict(orient="records")
            else:
                results = df.fillna("N/A").to_dict(orient="records")
            return jsonify({"results": results})

        except Exception as e:
            print("🔥 Failed to convert df to JSON:", e)
            return jsonify({"error": "Result formatting failed", "detail": str(e)}), 500

    except Exception as e:
        print("❌ API error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
