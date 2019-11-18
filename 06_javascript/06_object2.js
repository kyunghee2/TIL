//ES5
// var books =['자바스크립트 입문','장고 웹 프로그래밍']
// var comics = {
//   'DC':['Aquaman','Joker'],
//   'Marvel':['Avengers','Spider Man']
// }
// var magazines = null
// var bookShop = {
//   books: books,
//   comics: comics,
//   magazines:magazines
// }
// console.log(bookShop)
// console.log(typeof bookShop) // object
// console.log(bookShop.books[0])
//ES6(ECMAScript 6)
//객체의 key와 value가 똑같으면 -> 배열처럼 한번만 작성가능
var books =['자바스크립트 입문','장고 웹 프로그래밍']
var comics = {
  'DC':['Aquaman','Joker'],
  'Marvel':['Avengers','Spider Man']
}
var magazines = null
var bookShop = {
  books,
  comics,
  magazines,
}
console.log(bookShop)
console.log(typeof bookShop) // object
console.log(bookShop.books[0])

