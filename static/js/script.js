const regex = {
    alpha: /^[a-zA-Z]+$/,
    alpha_with_space: /^[a-zA-Z]+(\s[a-zA-Z]+)*$/,
    email: /^\w+@[a-zA-Z0-9]+?\.[a-zA-Z]{2,3}$/,
    number: /^[0-9]+$/
};

function normalize_name(string){
    return string.replace(/\s+/g, ' ').trim();
}
function is_alpha(string, msg, empty_msg) {
    string=normalize_name(string);
    return string ? (regex.alpha.test(string) ? "" : msg+"\n") : empty_msg+"\n";
}

function is_alpha_with_space(string, msg, empty_msg) {
    string=normalize_name(string);
    return string ? (regex.alpha_with_space.test(string) ? "" : msg+"\n") : empty_msg+"\n";
}

function is_name(string, msg, empty_msg) {
    string=normalize_name(string);
    return string ? (regex.alpha.test(string) || regex.alpha_with_space.test(string) ? "" : msg+"\n") : empty_msg+"\n";
}

function is_email(string, msg, empty_msg) {
    string=string.trim();
    return string ? (regex.email.test(string) ? "" : msg+"\n") : empty_msg+"\n";
}

function is_num(string, msg, empty_msg) {
    return string ? (regex.number.test(string) ? "" : msg+"\n") : empty_msg+"\n";
}

function is_matching(string1, string2, msg, empty_msg) {
    return string1 && string2 ? (string1 === string2 ? "" : msg+"\n") : empty_msg+"\n";
}


function is_min(string, msg, empty_msg) {
    return string ? (string.length >15 ? "" : msg+"\n") : empty_msg+"\n";
}
function notnull(string,empty_msg){
    return string?  (field==!"" ? True : False): empty_msg+"\n";
}

function user_registration() {
    let error_msg = "";
    let name = document.forms["user_registration"]["name"].value;
    let email = document.forms["user_registration"]["email"].value;
    let password0 = document.forms["user_registration"]["password0"].value;
    let password1 = document.forms["user_registration"]["password1"].value;

    error_msg += is_name(name.trim(), " Invalid name ", "Empty name ");
    error_msg += is_email(email.trim(), " Invalid email", "Empty email ");
    error_msg += is_matching(password0, password1, " Passwords do not match", "Empty password ");

    if (error_msg == "") {
        return true;
    } else {
        alert(error_msg);
        return false;
    }
}
function contact_form() {
    let error_msg = "";
    let name = document.forms["contact"]["name"].value;
    let email = document.forms["contact"]["email"].value;
    let msg = document.forms["contact"]["msg_body"].value;

    error_msg += is_name(name, " Invalid name ", "Empty name");
    error_msg += is_email(email, "Invalid email", "Empty email ");
    error_msg += is_min(msg, " minimum 15 letters required", "Empty message body");

    if (error_msg == "") {
        return true;
    } else {
        alert(error_msg);
        return false;
    }
}

function login_form() {
    let error_msg = "";

    let email = document.forms["login"]["email"].value;
    let password= document.forms["login"]["password"].value;

    error_msg += is_email(email, "Invalid email", "Empty email ");

    error_msg +=notnull(password,"Empty password");
    

    if (error_msg == "") {
        return true;
    } else {
        alert(error_msg);
        return false;
    }
}
