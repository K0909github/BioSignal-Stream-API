# BioSignal-Stream-API

研究で扱う生体信号（EEG/PPG）を、ブラウザやスマホアプリから送ると「集中度」「ストレス度」を返すAPIを学習用に実装したリポジトリです。

このリポジトリは、以下のスキルを1つにまとめて学べる構成になっています。
- FastAPIでの非同期API設計
- 前処理と推論パイプラインの組み立て
- PostgreSQLへのログ保存
- Dockerでの再現可能な環境構築

## 目的
- 生体信号の受信 → 前処理 → 推論 → 保存 という一連の流れを体験する
- 研究コードを「サービスとして提供できる形」に変換する力を身につける
- 面接で説明できる、実用的な設計・実装を作る

## 動かし方（最小構成）
### 1) 起動
```bash
docker compose up --build
```

### 2) 予測APIのテスト
```bash
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user-001",
    "device_id": "device-abc",
    "signal_type": "EEG",
    "sampling_rate": 256,
    "values": [0.1, 0.2, 0.15, 0.05, 0.0, -0.1, -0.05]
  }'
```

## API仕様（概要）
### POST /api/v1/predict
- 入力: 生体信号の時系列データとメタ情報
- 出力: 集中度・ストレス度・モデルバージョン・ログID

例:
```json
{
  "focus_score": 0.58,
  "stress_score": 0.42,
  "model_version": "stub-0.1.0",
  "log_id": 1
}
```

## フォルダ構成と役割
```
.
├── app/
│   ├── api/           # APIエンドポイント
│   ├── core/          # 設定読み込み
│   ├── db/            # DB接続と初期化
│   ├── models/        # DBテーブル定義
│   ├── schemas/       # 入出力の型定義
│   └── services/      # 前処理・推論・ログ保存
├── ml_engine/         # 前処理と推論の実装
├── docker/            # Dockerfile
├── tests/             # テスト（雛形）
└── docker-compose.yml
```

## 処理の流れ（初心者向けに簡単に）
1) クライアントが生体信号データを送信
2) APIがデータを検証し、前処理に渡す
3) 推論（今はスタブ）でスコアを出す
4) 推論結果をPostgreSQLに保存
5) 結果をレスポンスとして返す

## 各ファイルの解説（要点）
- app/main.py: FastAPIの起動設定とルーティング登録
- app/api/v1/predict.py: 予測APIの本体。前処理→推論→保存をまとめて実行
- app/core/config.py: DB接続設定を環境変数から読み込む
- app/db/session.py: 非同期DBセッションの作成
- app/db/init_db.py: 起動時にテーブル作成
- app/models/analysis_log.py: 解析ログのテーブル定義
- app/schemas/predict.py: リクエスト/レスポンスの型定義
- app/services/preprocess.py: 前処理の入口（本格処理はここに実装）
- app/services/inference.py: 推論フローの統合
- app/services/logger.py: DB保存処理
- ml_engine/preprocess.py: 最小限の特徴量抽出
- ml_engine/model_stub.py: 学習済みモデルの代わりの疑似推論
- docker-compose.yml: APIとDBを一括起動
- docker/app.Dockerfile: API用コンテナのビルド定義

## ここからの発展アイデア
- Mamba/U-Mambaモデルを組み込み、推論部分を置き換える
- 特徴量抽出をMNEやNeuroKitで本格化
- ユーザーごとの平均スコア集計APIを追加
- Alembicでマイグレーション管理
- 認証やレート制限を追加して商用に近づける
