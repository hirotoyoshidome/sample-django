# SampleDjango

## HelloWorld出力まで
djangoのインストールとかは事前に実施済みの想定

```
django-admin startproject sample
python3 manage.py startapp hello
```

hellp/viewsを編集してHelloWorldを出力するように修正する

プロジェクトディレクトリ配下のsettings.pyの
INSTALLED_APPSの部分に追加したアプリケーションを設定して認識させる

プロジェクト配下のurls.pyにルーティングの設定をしてパスに対してhelloアプリケーションの方を参照するように設定をする

```
python3 manage.py runserver
```

http://localhost:8000/hello/
にアクセスして正常に出力されるかを確認する

### ちょと触ってみてわかったこと
プロジェクトのディレクトリが

```
django-admin startproject {projectname}
```
のコマンドで生成される

上記のコマンドで生成されたディレクトリ配下のsettings.pyでアプリケーションの管理設定ができるみたい

urls.pyでルーティングの設定ができるが、参照しているのはプロジェクト配下のurls.pyである（自動で生成されるもの）

各アプリケーション配下にurls.pyを手動で生成してプロジェクト配下のurls.pyにincludeするのがベストプラクティス

viwes.pyでもpythonで記述するみたい（HTMLレベルで書けるらしいけどこれは未確認）
⇒.htmlファイルでテンプレートファイルを作成する（この中でPythonスクリプトを書くことができる）


## Model
* startappコマンドで生成されたディレクトリ配下（今回ではhello）にmodels.pyが存在しているためこのファイルにデータベースのスキーマに相当する記述を行う

※ `__str__` メソッドは実装しておくこと

※プロジェクトディレクトリ（今回ではsample）配下のsettings.pyファイルでDBについ設定することができるけど、今回は標準のSQLiteを使用する

* hello/models.pyにスキーマ情報を記載したら、sample/setting.pyのINSTALLED_APPの部分にHelloConfigを読み込む設定を追記する

* マイグレートファイルを作成する

```
python3 manage.py makemigrations hello
```

* マイグレートファイルのSQLの確認を実施する

```
python3 manage.py sqlmigrate hello 0001
```
※0001はマイグレーションファイルの番号で識別する

* マイグレートを実施する

```
python3 manage.py migrate
```

### model確認（おまけ）
* APIモードに入ってDBを操作してみる

```
python3 manage.py shell
```
下記コマンドで確認できる

```
>>> from hello.models import Choice, Question
>>> Question.objects.all()
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
>>> q.question_text
>>> q.pub_date
>>> quit
```

## admin画面(http://localhost:8000/admin)
* 下記コマンドでスーパーユーザを追加する

```
python3 manage.py createsuperuser
```
プロンプトに従ってユーザーを追加する

* hello/admin.pyに作成したスキーマ（models.pyに記載してあるclass）を読み込むように設定をする


* サーバーを起動してadmin画面にログインをすることで画面からDBを操作できるようになる

```
python3 manage.py runserver
http://localhost:8000/admin
```

## views
* 公式のチュートリアルに合わせるようにアプリケーション内のurls.py(hello/urls.py)をプロジェクトのurls.py(sample/urls.py)でincludeして読み込む

* /で区切った値を取得できるようにするためにhello/urls.pyに記載することで取得できるようになる

```
http://localhost:8000/hello
http://localhost:8000/hello/1/
http://localhost:8000/hello/1/results/
http://localhost:8000/hello/1/vote/
```
にアクセスすることでそれぞれのルーティングにアクセスすることが可能
