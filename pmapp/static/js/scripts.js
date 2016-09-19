// Empty JS for your own code to be here

$(function(){

    var obj=null;
    var As=$('ul.nav-left li');
    obj=As.eq(0);
    // alert(As.eq(0).children().eq(0).attr('href'))
    // alert(window.location.href)
    for(i=1;i<As.length;i++){if(window.location.href.indexOf(As.eq(i).children().eq(0).attr('href'))>=0) obj=As.eq(i)}
    obj.addClass('active');

    // $('ul.nav-left li a').click(function(e){
    //
    //  $(this).parent().addClass('active')
    //
    // });

    var $table = $('#table');
	$('#toolbar').find('select').change(function () {
    $table.bootstrapTable('refreshOptions', {
      exportDataType: $(this).val()
    });

  });

});
