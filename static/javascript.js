// alert('javascript is loaded');




$(document).ready(function(){
    $('td').on('click',function(){
          $(this).toggleClass('gray');
    });
// });



// $(function() {
//     $('a#calculate').bind('click', function() {
//         $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
//         a: $('input[name="a"]').val(),
//         b: $('input[name="b"]').val()
//         }, function(data) {
//         $("#result").text(data.result);
//         });
//         return false;
//     });
// });

// $(function() {
//   $('#current_bingo_num').bind('click', function() {
//       $.getJSON($SCRIPT_ROOT + '/_next_number', {
//       a: $('#current_bingo_num').val()
//       }, function(data) {
//       $("#current_bingo_num").text(data.result);
//       });
//       // socket.emit( 'my event', {MESSAGE : 'rt'});
//       // socket.on( 'my response', function( msg ) { $( 'div.testbing').append(msg.bingo) } );
//       return false;
//   });
// });

// $(document).ready(function(){
  var socket = io.connect('http://' + document.domain + ':' + location.port);
  var bingo_num_for_newcomers 

  $(function() {
    $('#btn_next_ball').bind('click', function(e) {
        socket.emit( 'get ball', {}); //MESSAGE : 'get a ball'
        // $("p:first").replaceWith("Hello world!")
        // $( '#current_bingo_num' ).text( '' );
        // socket.on( 'my bingo response', function( msg ) { $( '#current_bingo_num').text(+msg.bingo)} );  //; bingo_num_for_newcomers = text(+msg.bingo)
        
        // bingo_num_for_newcomers = $( '#current_bingo_num' ).text( );

        // console.log(bingo_num_for_newcomers);
        // $.getJSON($SCRIPT_ROOT + '/_next_number', {
        // // a: $('#current_bingo_num').val()
        // }, function(data) {
        // $("#current_bingo_num").text(data.result);
        // });

        return false;
    });
  });

  socket.on( 'my bingo response', function( msg ) { 
    $( '#current_bingo_num').text(+msg.bingo)
  });

  // $("#btn_next_ball").click(function(){
  //     num = 0 // parseInt($(".figure").text());
  //     $(".figure").text("{{ next_ball[" + num + "] }}" );
  //     num = num+1
  // })


  // https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d
  // var socket = io.connect('http://' + document.domain + ':' + location.port);

  socket.on( 'connect', function() {
    socket.emit( 'connect event', {
      data: 'User Connectedddddd'
    } )
    
    
      socket.on( 'my connect response', function( msg ) { 
        console.log(msg.c_ball_val)
        if( msg.c_ball_val !== 0 ) {
          $( '#current_bingo_num').text(msg.c_ball_val)
        }
      } );
    

    // if( bingo_num_for_newcomers !== 'undefined' ) {
    //   $( '#current_bingo_num').text(bingo_num_for_newcomers)
    // }
    // console.log(bingo_num_for_newcomers)
    // $( '#current_bingo_num').text('testing')
  } )

  var form = $( 'form' ).on( 'submit', function( e ) {
    e.preventDefault()
    let user_name = $( 'input.username' ).val()
    let user_input = $( 'input.message' ).val()
    socket.emit( 'my event', {
      user_name : user_name,
      message : user_input
    } )
    $( 'input.message' ).val( '' ).focus()
  } )

  // } )  MOVED TO ABOVE. 'connect' function just to see the difference. nothing obvious, looks tidier


  // $(function() {
  //   $('#current_bingo_num').bind('click', function() {
  //       $.getJSON($SCRIPT_ROOT + '/_next_number', {
  //       a: $('#current_bingo_num').val()
  //       }, function(data) {
  //       $("#current_bingo_num").text(data.result);
  //       });
  //       // socket.emit( 'my event', {message : 'rt'});
  //       // socket.on( 'my response', function( msg ) { $( 'div.testbing').append(msg.bingo) } );
  //       return false; 
  //   });
  // });







  socket.on( 'my chat response', function( msg ) {
    // console.log( msg )
    if( typeof msg.user_name !== 'undefined' ) {
      // $( 'h3' ).remove()
      $( 'div.message_holder' ).append( '<b style="color: #000">'+msg.user_name+'</b>'  + ' : '+ msg.message + '<br/>') 
      // $( '#current_bingo_num' ).text( msg.message ) 

      // $( 'div.bingo_holder').append(msg.bingo)
    }
  })
});