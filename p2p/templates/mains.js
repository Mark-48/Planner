
function pst() {
  const user = {
    "name": "Ivan Ivanov",
    "username": "ivan2002",
    "email": "ivan2002@mail.com",
  };

  const Http = new XMLHttpRequest();
  const url='http://127.0.0.1:5000/data_post';
  alert('ЗДАРОВ БАНДИТЫ');
  Http.open("POST", url);
  Http.setRequestHeader("Content-Type", "application/json");
  Http.send(JSON.stringify(user));

}

