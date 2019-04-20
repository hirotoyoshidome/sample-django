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

各アプリケーション配下にurls.pyを手動で生成してプロジェクト配下のurls.pyにincludeするのがベストプラクティス？？

viwes.pyでもpythonで記述するみたい（HTMLレベルで書けるらしいけどこれは未確認）

```
python manage.py migrate
```
コマンドを実行したら自動でマイグレートをしてくれる？？

細かい処理のファイルをどの部分に配置するとかのベストプラクティスは不明

データベースアクセス部分(DAO)に関しても未確認



