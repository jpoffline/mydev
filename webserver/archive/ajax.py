def get_ajax():
    return '''
    <script>
        $('#post').click(function(){
            $.ajax('/post', {
                method: 'POST',
                timeout: 1000,
                data: {
                    message: $('#input').val(), 
                    sent_by: $('#username').val()
                }
            });
        });
        var last_message = '';
        (function poll() {
            $.ajax('/poll', {
                method: 'POST',
                timeout: 1000*60*10, //10 minutes
                success: function(data){
                    
                    $("<p>"+data+"</p>").appendTo($(document.body));
                    last_message = data;
                    poll();
                },
                error: function(){
                    setTimeout(poll, 1000);
                },
                data: last_message
            });
        }());
        </script>
        '''
def get_html(path):
    print 'HTML ', path
    if path=='' or path=='index.html':
        return '''
        <body>
        <style>
        iframe {
            width: 400px;
            height: 600px;
        }
        </style>
        <iframe src="room.html"></iframe>
        </body>
        '''
    elif path=='room.html':
        return '''
        <body>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
        <input id="username" value="jp"/>
        <input id="input"/>
        <button id="post">post</button>
        ''' + get_ajax() + '''
        </body>
        '''