# -*- coding: utf-8 -*-

import azure.cognitiveservices.speech as speechsdk
import dotenv


def main():

    # Speech serviceの設定
    speech_key = dotenv.dotenv_values('.env')['SPEECH_SERVICE_KEY']
    service_region = dotenv.dotenv_values('.env')['SPEECH_SERVICE_REGION']
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # 使用する音声フォントの指定
    speech_config.speech_synthesis_voice_name = 'ja-JP-NanamiNeural'

    # 出力ファイルの形式を設定（オプション）
    speech_config.speech_synthesis_output_format = speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3

    # 音声ファイルに合成するための設定
    audio_config = speechsdk.audio.AudioOutputConfig(filename="./output/output_audio.mp3")

    # SpeechSynthesizerのインスタンスを作成
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # テキストを音声に合成し、指定されたファイルに保存
    text = "このデモでは、BLOBとストレージアカウントをどうやって作るかを見ていきますね。BLOBをアップロードしたい場合、まずストレージアカウントが必要になります。それがスタート地点です。ストレージアカウントというサービスを探さないといけません。以前のデモでやったように、プラスボタンを使ってリソースを作成します。「作成」を選択して、サブスクリプションとリソースグループについての情報を入力します。VMを作った時に作成したリソースグループを使えますね。その後、世界中でユニークなストレージアカウント名を決めないといけません。名前はAzure内の既存のストレージアカウント名と全く同じであってはいけません。そうしないと、ストレージアカウントを作成できません。「SandraLongName」というようなユニークな名前を選んで、確実にユニークであることを確認して、問題なく進められるようにします。これで先に進めますね。同じ地域を選びます、なぜなら私の近くだからです。そして、パフォーマンスを選択します。標準ですか、それともプレミアムですか？低遅延が必要ならプレミアムを選びたいですが、標準でも問題ありません。そして、冗長性のオプションを選ぶ必要があります。LRS、GRS、ZRS、そしてGZRSを議論した冗長性オプション全てがあります。デモ用だから、一番安いLRSを選びます。そして、AZ-900試験に合格するためには知らなくても大丈夫ですが、セキュリティを強化したい場合には、追加機能があることを知っておく必要があります。その後はネットワーキングです。デフォルトで、全てのネットワークから公開アクセスができるようにします。でも、特定の仮想ネットワークからのみアクセスを許可したい場合は、ここで選べますし、特定のIPアドレスからのみアクセスを許可したい場合も、設定できます。このページにはデータ保護のオプションがあり、ソフトデリートが特に興味深いです。ソフトデリートは、アイテム（例えばBLOB）を削除しても、デフォルトで7日間は「ごみ箱」に保持され、誤って削除からデータを保護できるってことです。必要に応じて日数を変更もできます。このページには暗号化のオプションもあります。例えば、暗号化のためにカスタム管理キーを使いたい場合でも大丈夫です。AZ-900の範囲を少し超えますが、高度なオプションがあります。ここには、以前のリソース作成時にあったタグもあります。それからレビューして、ストレージアカウントを作成できます。「作成」を押してデプロイメントを開始し、通常、ストレージアカウントの作成には1〜2分かかります。その後、中に入ってコンテナを作成し、BLOBを追加できます。デプロイメントが進行中です。ちょっと待ちましょう。素晴らしいですね。リソースが作成されました。さあ、ストレージアカウントに行きましょう。ここに概要があり、データストレージには4つの異なるオプションがあります。コンテナ、ファイルシェア、キュー、テーブルです。BLOBの作成には、コンテナを使う必要があります。だから、データストレージの中のコンテナを選んで、プラスボタンで新しいコンテナを追加します。コンテナを選んで、一意な名前を付けます。そして、異なる公開アクセスレベルがありますね。プライベート（匿名アクセスなし）、BLOB（BLOBのみの匿名読み取りアクセス）、またはコンテナ（コンテナとBLOBの両方への匿名読み取りアクセスを提供）。このデモでは、私たちのコンテナとBLOBが匿名でアクセスされないようにプライベートを選びます。必要であれば、暗号化や追加機能を設定することもできますが、このシンプルなデモでは、公開アクセスをプライベートに設定して、コンテナを作成します。その後、コンテナの中に入ってBLOBをアップロードできます。中で、ファイルを選んで、アップロードをクリックします。これで、BLOBが無事にアップロードされました。そして今、それを共有したいとしましょう。私のBLOBへのリンクがここにありますが、プライベートアクセスなので、外部のユーザーと共有したい場合は、キーを生成する必要がありますね。ここにSASがあります。なので、組織の外の誰かにこの画像を見せたい場合は、SASを生成して、プライベートアクセスの私のBLOBに一時的なアクセスを提供できます。パーミッションを選ぶことが重要です。このBLOBに対する読み取り専用アクセスを許可し、アクセスが有効な期間を指定します。そして、組織の外部のこの画像への一時的なアクセスを持つために、SASトークンを生成します。そしてそれをテストするために、新しいプライベートタブを開いて、画像にアクセスしてみましょう。そしてここに「Keep calm and configure Azure.」の素敵なメッセージが表示されます。これが今日、私たちが一緒に学んでいることです。このデモを見てくれてありがとうございました。私たちは、まずストレージアカウントを作成し、その後コンテナを作って、BLOBをアップロードし、SASを使って特定の期間だけ共有する方法を見ました。ご覧いただきありがとうございました。さあ、プレゼンテーションに戻りましょう。"

    result = speech_synthesizer.speak_text_async(text).get()

    # 結果をチェック
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Audio file is saved to output_audio.mp3")
    else:
        print(f"Speech synthesis canceled: {result.cancellation_details.reason}")
        if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            if result.cancellation_details.error_details:
                print(f"Error details: {result.cancellation_details.error_details}")



if __name__ == "__main__":
    main()