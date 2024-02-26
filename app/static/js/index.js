// Flash dismiss
function flashDismiss(id){
    document.getElementById(`flash-${id}`).remove();
};

// Toggling required field
function fileOrLinkToggle(){
    const checkbox = document.getElementById('file-or-link');
    const link_input = document.getElementById('original-url');
    const file_input = document.getElementById('to-upload');

    if(checkbox.checked){
        link_input.removeAttribute('required');
        file_input.setAttribute('required', true);
    }
    else{
        link_input.setAttribute('required', true);
        file_input.removeAttribute('required');
    };
};

// Dialogs handling
function openDialog(route, message){
    document.getElementsByTagName('dialog')[0].showModal();
    document.getElementsByTagName('dialog')[0].style.display = 'flex';
    document.getElementById('dialog-message').innerText = message;
    document.getElementById('dialog-confirm').setAttribute('href', route);
};
function closeDialog(){
    document.getElementsByTagName('dialog')[0].close();
    document.getElementsByTagName('dialog')[0].style.display = 'none';
};

// Exporting the new link to user's clipboard
function toClipboard(new_link){
    navigator.clipboard.writeText(new_link);
    document.getElementById('new-link').innerText = "Copié !";
};

// Responsive navbar button handling
function responsiveMenuDisplay(){
    const navbar = document.getElementsByTagName('nav')[0];
    const header = document.getElementsByTagName('header')[0];

    if(navbar.className === 'navbar'){
        navbar.className += ' responsive';
        header.style.backgroundColor = 'rgb(20, 30, 40)';
    }
    else{
        navbar.className = 'navbar';
        header.style.backgroundColor = 'rgb(30, 40, 50)';
    };
};