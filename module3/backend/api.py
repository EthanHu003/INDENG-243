import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from model_code import match_houses

app = Flask(__name__)
# 更宽松的 CORS 配置
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    query = data.get("query", "")

    try:
        df = match_houses(query)
        if df is None or df.empty:
            return jsonify({"results": []})

        # 确保所有需要的列都存在
        required_columns = ['ADDRESS', 'RENT_PRICE', 'SQFT', 'BEDS', 'BATHS', 'BUILDING_TYPE',
                          'Shopping', 'Food & Dining', 'Fitness & Recreation',
                          'POOL', 'GYM', 'GARAGE', 'FURNISHED', 'DOORMAN', 'CLUBHOUSE']
        
        # 添加经纬度字段（如果没有）
        if 'latitude' not in df.columns or 'longitude' not in df.columns:
            # 添加随机位置（仅示例，实际应该从数据获取）
            import numpy as np
            df['latitude'] = 39.9526 + (np.random.rand(len(df)) * 0.02 - 0.01)
            df['longitude'] = -75.1652 + (np.random.rand(len(df)) * 0.02 - 0.01)

        # 格式化 amenities
        amenities_cols = ['POOL', 'GYM', 'GARAGE', 'FURNISHED', 'DOORMAN', 'CLUBHOUSE']
        df['amenities'] = df.apply(lambda row: ', '.join([col for col in amenities_cols if row.get(col) == 'Y']), axis=1)

        # 格式化分数
        score_cols = ['Shopping', 'Food & Dining', 'Fitness & Recreation']
        df['scores'] = df.apply(lambda row: {col: row[col] for col in score_cols if col in row and pd.notna(row[col])}, axis=1)

        # 选择要返回的列
        return_cols = required_columns + ['latitude', 'longitude', 'amenities', 'scores']
        available_cols = [col for col in return_cols if col in df.columns]
        
        results = df[available_cols].fillna("N/A").to_dict(orient="records")
        return jsonify({"results": results})

    except Exception as e:
        print("❌ API error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)  # 明确指定端口