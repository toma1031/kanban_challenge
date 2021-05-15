// フォームのカード自体をdivタグで囲み
// 囲うのに使用したdivタグにはformというidとd-noneというクラスを付与した。
// d-noneクラスは要素を隠すbootstrapのクラスです。
//  + add cardをクリックしたらそのid="form"の要素からd-noneを削除するという操作をmain.jsに追加した。
$('button').on('click', () => {
  $('#form').removeClass('d-none');
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