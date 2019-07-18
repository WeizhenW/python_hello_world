$(document).ready(onReady);

function onReady() {
    console.log('in jq');
    newFruit = $()
    $.ajax({
        type: 'POST',
        url: '/',
        data: {'fruit': 'orange'}
    }).then(() => {
        $.ajax({
            type: 'GET',
            url: '/',
        })
    })
}