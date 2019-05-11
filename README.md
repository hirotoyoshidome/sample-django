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

### 最初だけ実施するコマンド＆わかったこと
プロジェクトのディレクトリが

```
django-admin startproject {projectname}
```
のコマンドで生成される

上記のコマンドで生成されたディレクトリ配下のsettings.pyでアプリケーションの管理設定ができるみたい

urls.pyでルーティングの設定ができるが、参照しているのはプロジェクト配下のurls.pyである（自動で生成されるもの）

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

## View
* 公式のチュートリアルに合わせるようにアプリケーション内のurls.py(hello/urls.py)をプロジェクトのurls.py(sample/urls.py)でincludeして読み込む

* /で区切った値を取得できるようにするためにhello/urls.pyに記載することで取得できるようになる

```
http://localhost:8000/hello
http://localhost:8000/hello/1/
http://localhost:8000/hello/1/results/
http://localhost:8000/hello/1/vote/
```
にアクセスすることでそれぞれのルーティングにアクセスすることが可能

* テンプレートファイルを使用して読み込むとき変数は{{ var  }}のような感じで読み込むことができる

* 画面に出力しないものに関しては{% if  %}{% endif %}, {% for %}{% endfor %}のような感じで簡単な分岐、ループができる

* renderメソッドを使用することで簡単にテンプレートにレンダリングすることができ、引数で辞書型の値を渡すことでテンプレートファイルから変数を使用できるようになる

* テンプレートファイルではハードコーディングしたくないため、urlメソッドを使用してviews.pyのメソッド名を渡すことでパスを記載する

* 名前空間(app_nameで定義)を使用することで同一名でもきれいにまとめられる

## form関連
* templateの部分でfor文のインデックスを取得したい場合は{{ forloop.counter }}を使用することで取得できる

* formを作成する場合は、HTML標準のタグを使用して、その中でpythonを記述することができる

* CSRF対策として{% csrf_token %}を記述することでトークンが自動的に設定できる（formタグ内に記載すること）

* MTVモデルのためコントローラの概念はなくViewのファイルに処理を記載すること

* Question : Choice = 1 : nの関係に紐づくようにModelファイルで外部キーが設定されているため、管理画面(admin)からデータをインサートして投票の確認をすることができる

* リダイレクト処理をするときにreverseメソッドを使用することでハードコーディングを防ぐことができるため、使用すること

## 汎用ビュー
* Djangoには標準で汎用的に使用できるViewが用意されている
参考：https://docs.djangoproject.com/ja/2.2/ref/class-based-views/

* urls.pyで汎用のビューを継承したviews.pyに定義されたclassを指定することで簡単簡潔に処理を記載することができる

* urls.pyのpkはプライマリーキーのことでDetailView内で使用される値のためquestion_idから変更して、記載している

* views.pyでは継承したクラスを設定するため、class定義の引数に継承する汎用ビューのクラスを記載する

* template_nameにはテンプレートの名前を設定する

* modelにはモデルクラスを指定する

* 定義したget_querysetメソッドをcontext_object_nameで設定したlistの呼び出しの際に呼び出されている（裏で上書きがされている）

## テストコード
* アプリケーションのディレクトリのtests.pyにテストケースを記述する

* テストを実行する場合は下記にコマンドを実行する

```
python3 manage.py test hello
```

※参考：https://docs.djangoproject.com/ja/2.2/topics/testing/


## 静的コンテンツ
* cssを導入するときは
hello/static/hello/style.css
のようにディレクトリを切って配置してstaticメソッドをテンプレートで使用して絶対パスを指定する
それを使用してcssファイルを読み込むように設定をする

## 管理画面
* hello/admin.pyを編集することで管理画面の出力方法を変更することができる

* カラムの出力順序やリレーションの貼られているモデルの表示方式、レコードの出力方式、フィルター、検索機能を追加することができる（実装済み）

* 管理画面のテンプレートは

```
python -c "import django; print(django.__path__)"
```
コマンドでdjangoのソースファイルの場所を確認して、`django/contrib/admin/templates` 配下に存在している。

これをsample/settings.pyのTEMPLATESのdirで設定したディレクトリ（今回はtemplates/配下）に同様のディレクトリ階層で配置することで上書きをすることができる

## パッケージング
アプリケーションをパッケージングすることで再利用可能とする

```
pip3 install setuptoola
```
を事前にインストールしておく

* アプリケーションのディレクトリごと外部のディレクトリに移動する

```
cd sampleDjango
mkdir ../django-hello
mv hello/ ../django-hello/
```

* README.rstを作成する

```
cd ../django-hello
touch README.rst
vi README.rst
```

* LICENSEファイルを作成する
⇒　公開する際はライセンスをつけること
⇒　多くはBSDライセンスの元に配布される

```
touch LICENSE
vi LICENSE
```

* setup.pyを作成する
アプリケーションがどのようにビルド・インストールされるかを提供するもの

