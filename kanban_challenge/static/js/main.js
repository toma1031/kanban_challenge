// フォームのカード自体をdivタグで囲み
// 囲うのに使用したdivタグにはformというidとd-noneというクラスを付与した。
// d-noneクラスは要素を隠すbootstrapのクラスです。
//  + add cardをクリックしたらそのid="form"の要素からd-noneを削除するという操作をmain.jsに追加した。
$('button').on('click', () => {
  $('#form').removeClass('d-none');

// XMLHttpRequestオブジェクトの作成
var request = new XMLHttpRequest();

// URLを開く
request.open('GET', 'https://randomuser.me/api/?results=25', true);
request.responseType = 'json';

// レスポンスが返ってきた時の処理を記述 
request.onload = function () {
  // レスポンスが返ってきた時の処理
  var data = this.response;
  // console.log(data)
for (var i = 0;  i < 25;  i++) {
    // 繰り返し処理
    var first_name = (data['results'][i]['name']['first']);
    var last_name = (data['results'][i]['name']['last']);

    // FirstNameとLastNameを横一列に並べるため以下のように書く
    full_name = first_name + ' ' +last_name
    // outputのidがついているoptionタグを取得
    // 変数を埋め込む文字列は'(バッククオート)で囲む
    // 埋め込む変数は${}で囲む
    // 次のように書くことで、element要素の内容を削除した後、変数full_nameの内容をelement要素に表示する事が可能です。
    $(`#output${i}`).html(full_name);
   }
}
// リクエストをURLに送信
request.send()
});

// クリックされた時、アラートを出す
$('.fa-chevron-right').click(function () {
  // 矢印がクリックされたら、data-idの値を取得、その値をDjango側に送信し
  // alert($(this).data('id'))
  // alert($(this).data('status'))
  var plus_status = $(this).data('status') + 1;
  // 該当オブジェクトのstatusを更新する???
  $('<form/>',{action:`${$(this).data('href')}`, method:"post"})
  .append(`<input type='hidden' name='data-id'value='${$(this).data('id')}'>`)
  .append(`<input type='hidden' name='status-id'value='${ plus_status }'>`)
  .append(`<input type='hidden' name='href-id'value='${$(this).data('href')}'>`)
  .append(`<input type='hidden' name='csrfmiddlewaretoken'value='${$(this).data('csrf')}'>`)
  .appendTo($('body'))
  .submit();
});


$('.fa-chevron-left').click(function () {
  // 矢印がクリックされたら、data-idの値を取得、その値をDjango側に送信し
  // alert($(this).data('id'))
  // alert($(this).data('status'))
  var minus_status = $(this).data('status') -1 
  // 該当オブジェクトのstatusを更新する???
  $('<form/>',{action:`${$(this).data('href')}`, method:"post"})
  .append(`<input type='hidden' name='data-id'value='${$(this).data('id')}'>`)
  .append(`<input type='hidden' name='status-id'value='${ minus_status }'>`)
  .append(`<input type='hidden' name='href-id'value='${$(this).data('href')}'>`)
  .append(`<input type='hidden' name='csrfmiddlewaretoken'value='${$(this).data('csrf')}'>`)
  .appendTo($('body'))
  .submit();
});