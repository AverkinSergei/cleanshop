Vue.component('todo-item', {
    props: ['todo'],
    template: '<li>{{ todo.text }}</li>'
})

var app = new Vue({
    el: '#app',
    data: {
        message: "Вы загрузили страницу " + new Date().toLocaleString(),
        message1: "Message1",
        message2: "Hello, Vue.js!",
        seen: true,
        todos: [
            {text: 'text 1'},
            {text: 'text 2'},
            {text: 'text 3'}
        ],
        groceryList: [
            {id: 1, text: 'Овощи'},
            {id: 2, text: 'Фрукты'},
            {id: 3, text: 'Что-то там еще'}
        ]
    },
    methods: {
        reverseMessage: function () {
            this.message1 = this.message1.split('').reverse().join('');
        }
    }
});