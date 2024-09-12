const fetchPromise = fetch(
    "http://127.0.0.1:5000/tasks",
  );
  
  fetchPromise
    .then((response) => response.json())
    .then((data) => {
      console.log(data[0].name);
    });

  
