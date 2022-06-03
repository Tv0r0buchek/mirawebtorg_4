let green = function () {
    $('.header-radius').css('background-color', 'green')
    setTimeout(white, 9000)
}

let white = function () {
    $('.header-radius').css('background-color', 'white')
}

let red = function () {
    $('.header-radius').css('background-color', 'red')
    setTimeout(white, 9000)
}

function productAdded_basket_dialog_show(message) {
    $(`body`).css("overflow", "hidden")
    $(`.dialog_window_background`).css("display", "block")
    $(`.product_added_into_basket_msg`).css('display', "block")
    if (message === "product_added") {
        $('.message_product_added').css("display", "block")
    } else if (message === "product_already_exists") {
        $('.message_product_already_added').css("display", "block")
    }
}

function productAdded_basket_dialog_hide() {
    $("body").css('overflow', '')
    $(".dialog_window_background").css("display", "")
    $('.product_added_into_basket_msg').css("display", "none")
    $(`.message_product_added`).css("display", "none")
    $(`.message_product_already_added`).css("display", "none")
}

$(`.button_stay_here`).on("click", () => productAdded_basket_dialog_hide())