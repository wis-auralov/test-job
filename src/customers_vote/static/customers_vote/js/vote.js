function customer_vote(){
    var a = $(this);
    var url = a.attr('href');

    $.post(url).success(function(data){
        if (!data['vote_active']){
            alert('голосование за данного пользователя окончено');
        }
        $('.vote-counter', a.parent()).html(data['vote_count']);
    });

    return false;
}

$(document).on('click', 'a.vote-btn', customer_vote);