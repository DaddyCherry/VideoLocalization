import os
import requests
import dotenv


# 環境変数からエンドポイントとAPIキーを取得
azure_openai_endpoint = dotenv.dotenv_values('.env')['AZURE_OPENAI_ENDPOINT']
azure_openai_api_key = dotenv.dotenv_values('.env')['AZURE_OPENAI_API_KEY']

# リクエストのパラメータを設定
deployment_name = "demo-tts-hd"
model = "tts-1-hd"
voice = "alloy"
language = "Japanese"
input_text = '''まず、さまざまなストレージサービスに慣れることから始めましょう。​

Azure Storage アカウントと、それが利用可能なさまざまなストレージ サービスとどのように関連しているかについて説明します。​

また、ストレージ層の拡張、データ冗長性オプション、データやインフラストラクチャ全体を Azure に移行する方法についても説明します。​

それでは、ストレージ アカウントから始めて、データ ストレージについて詳しく見ていきましょう。​

ストレージ アカウントは、Azure Storage サービス内のデータに一意の名前空間を提供し、HTTP または https://protocols を介して世界中のどこからでもアクセスできます。​

Azure Storage アカウントには、Azure Storage Services のすべてのデータ オブジェクト、大きなバイナリ オブジェクトまたは BLOB、ファイル、キュー、テーブルが含まれます。​

ストレージ アカウント内のデータは保護され、可用性が高く、信頼性が高く、スケーラブルです。​

ストレージ アカウントを作成するときは、まずアカウントの種類を選択する必要があります。​

アカウントの種類はストレージ サービスに影響し、冗長性オプションは使用方法に影響します。​

しかし、冗長性オプションとはどういう意味ですか?​

ストレージには、ハードウェア、ネットワーク、電源障害などの計画的または計画外のイベントから保護するために、常に複数のデータのコピーが格納されます。​

自然災害と冗長性の向上により、障害が発生した場合でも、ストレージ アカウントがターゲットの可用性と持続性を満たすことが保証されます。​

シナリオに最適な冗長性オプションを決定し、コストと高可用性の最適なバランスを見つけるために、LRS はローカル冗長ストレージを 3 回レプリケートします。​

LRS は、プライマリ リージョンの 1 つのデータ センターを使用して、少なくとも 99 ポイント 999999% (特定の年間で 11 9 分の 1) のオブジェクトの耐久性を保証します。​'''

# リクエストのURLを作成
url = f"{azure_openai_endpoint}/openai/deployments/{deployment_name}/audio/speech?api-version=2024-02-15-preview"

# リクエストのヘッダーを設定
headers = {
    "api-key": azure_openai_api_key,
    "Content-Type": "application/json"
}

# リクエストのボディを設定
data = {
    "model": model,
    "input": input_text,
    "voice": voice,
    "language": language
}

# リクエストを送信
response = requests.post(url, headers=headers, json=data)

# レスポンスのステータスコードをチェック
if response.status_code == 200:
    # 音声データを保存
    with open("speech.mp3", "wb") as f:
        f.write(response.content)
    print("音声が正常に生成され、speech.mp3に保存されました。")
else:
    print(f"リクエストが失敗しました。ステータスコード: {response.status_code}")
    print(f"エラーメッセージ: {response.text}")