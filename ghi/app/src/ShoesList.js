async function ShoesList() {
    const response = await fetch('http://localhost:8080/api/shoes/');
    console.log(response);
  }
  ShoesList();
