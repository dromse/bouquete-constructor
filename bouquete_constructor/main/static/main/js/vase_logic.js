var items = [];
var counter = 0;

function deseneazaTabel() {
    if (items.length === 0) {
        document.getElementById("list").style.display = "none";
    } else {
        document.getElementById("list").style.display = "";
    }
    var str = "";
    var button = "";
    for (var i = 0; i < items.length; i++) {
        str += `<tr id=${i}>
           <td>${items[i].item}</td>
           <td><button onclick="deleteItem(${i})">Delete</button></td>
           </tr>`;
        button = `#id_b_delete`;
        document.querySelector(button).onclick = (id = i) => {
            items.splice(id, 1);
            console.log("Items - after deleting", items);
            deseneazaTabel();
        }
    }
    counter = i;
    document.querySelector("table tbody").innerHTML = str;
}


function addItem(form, event) {
    var item = {};
    var input = form.querySelectorAll("input[name]");

    var v = input[0].value;
    item["item"] = v;

    items.push(item);

    document.getElementById("list").classList.remove("hidden");
    deseneazaTabel();

    console.log("Items - ", items);
    console.log("Counter our id - ", counter);
    console.log("Input text - ", v);

    event.preventDefault();
}

function deleteItem(trId) {
    items.splice(trId, 1);
    console.log("Items - after deleting", items);
    deseneazaTabel();
}
