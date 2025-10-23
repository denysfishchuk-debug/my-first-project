const list = ["Döner", "BMW", "Audi", "VW", "Ubuntu"];

console.log("First :", list[0]);
console.log("Last :", list[list.length - 1]);
console.log("3: ", list[2]);

console.log("forEach: ---------------------------");
list.forEach((x) => console.log(x));

console.log("map: ---------------------------");
console.table(list.map((x) => x.toUpperCase() + " cool"));

console.log("obj: ---------------------------");
const user = {
  userName: "Denis",
  age: 29,
  city: "Odessa",
};

console.log("userName: " + user.userName);
console.log("age: " + user.age);
console.log("city: " + user.city);

user.food = "Döner";
console.log("food: " + user.food);

delete user.city;

console.log("deleted city: " + user.city); //undefined
console.table(user);

console.log("products: ---------------------------");
const products = [
  { id: 1, name: "Laptop", price: 3, available: true },
  { id: 2, name: "Headphones", price: 5, available: false },
  { id: 3, name: "Webcam", price: 39.99, available: true },
];

console.table(products.find((product) => product.id === 2));
console.log("products list : ---------------------------");
products.forEach((product) => console.table(product));
console.log("available list : ---------------------------");
console.table(products.filter((product) => product.available));

console.log("An Object with an Array: : ---------------------------");
const company = {
  name: "Döner GmbH",
  location: "Berlin",
  employees: [
    { firstName: "Anna", lastName: "Naß", department: "Engineering" },
    { firstName: "John", lastName: "Cena", department: "Kollektor" },
  ],
};

console.log("Company Name:", company.name);
const AnnaNaß = company.employees[0];
console.log("First Employee Name:", AnnaNaß.firstName, AnnaNaß.lastName);

company.employees.push({
  firstName: "Angela",
  lastName: "Merkel",
  department: "DHL Fahrer",
});

// console.table(company.employees)
console.table("full list------------------------------");
console.table("firstName lastName department");
company.employees.forEach((x) =>
  console.log(x.firstName, x.lastName, x.department)
);

console.log("products 3 ");
// console.table(products)
products.push({ id: 4, name: "lalala Task3 ", price: 149.99, available: true });
console.table(products);
const index = products.findIndex((product) => product.id === 2);
delete products[index];

products[3].price = 1;

console.table(products);
console.log("company---------------------------------------------------------");
company.employees[
  company.employees.findIndex((emp) => emp.firstName === "John")
].department = "Logistik";

console.table(company.employees);
