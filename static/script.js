$(document).ready(onReady);

function onReady() {
    console.log('in jq');
    $.ajax({
        type: 'POST',
        url: '/',
        data: 4
    }).then(() => {
        $.ajax({
            type: 'GET',
            url: '/',
        })
    })
}