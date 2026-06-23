import { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);

useEffect(() => {
  fetch("http://localhost:8001/products")
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      setProducts(data);
    });
}, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>CodeVector Product Browser</h1>

      {products.map((p) => (
        <div
          key={p.id}
          style={{
            border: "1px solid #ccc",
            margin: "10px",
            padding: "10px",
          }}
        >
          <h3>{p.name}</h3>
          <p>Category: {p.category}</p>
          <p>Price: ₹{p.price}</p>
        </div>
      ))}
    </div>
  );
}

export default App;