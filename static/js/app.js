function showElement(id) {
    document.getElementById(id).classList.remove('collapse');
}

function hideElement(id) {
    document.getElementById(id).classList.add('collapse');
}

function scrollTo(id) {
    document.getElementById(id).scrollIntoView({behavior: "smooth"});
}

function checkText() {
    if (document.getElementById('srcText').value.length === 0) {
        return false;
    } else {
        return true;
    }
}

function checkKey() {
    if (document.getElementById('key').value.length === 0) {
        return false;
    } else {
        return true;
    }
}


function pasteClick() {
    if (navigator.clipboard != undefined && navigator.clipboard.readText != null) {
        navigator.clipboard.readText().then(function (text) {
            document.getElementById("srcText").value = text;

        }).catch(function () {
            alert('Failed to read from clipboard. Access denied.');
        });
    } else {
        var savedtext = document.cookie.match('(^|;)\s?savedtext=([^;]*)(;|$)');
        if (savedtext) {
            document.getElementById("srcText").value = decodeURIComponent(savedtext[2]);
        }
    }
}

function uploadClick() {
    document.getElementById('fileUpload').click();
}


document.getElementById('fileUpload').addEventListener('change', function (event) {

    if (event.target.files.length > 0) {
        var file = event.target.files[0];

        if (file.type === "text/plain") {
            var reader = new FileReader();

            reader.onload = function (e) {
                var content = e.target.result;
                document.querySelector('.input').value = content;
            };

            reader.readAsText(file);
        } else {
            console.log("Please upload a .txt file.");
        }
    }
});


function copyClick() {

    var selectedText = document.querySelector('.output').value;

    if (selectedText !== "") {
        navigator.clipboard.writeText(selectedText).then(function () {
            console.log('Text successfully copied to clipboard');
        }).catch(function (err) {
            console.error('Could not copy text: ', err);
        });
    }
}


function downloadClick() {

    var selectedText = document.querySelector('.output').value;


    var blob = new Blob([selectedText], {type: 'text/plain'});


    var downloadUrl = URL.createObjectURL(blob);


    var downloadLink = document.createElement('a');
    downloadLink.href = downloadUrl;
    downloadLink.download = document.getElementById('resultLabel').innerText + ".txt"; // 文件名


    document.body.appendChild(downloadLink);
    downloadLink.click();


    document.body.removeChild(downloadLink);
    URL.revokeObjectURL(downloadUrl);
}