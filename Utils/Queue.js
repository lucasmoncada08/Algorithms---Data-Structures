/**
 * Queue functionality including simple enqueing and dequeing.
 */
class Queue {
    constructor() {
        this.elements = new Map();
        this.head = 0;
        this.tail = 0;
    }

    enqueue(element) {
        this.elements.set(this.tail, element);
        this.tail++;
    }

    deque() {
        if (this.head === this.tail) throw "Cannot deque with empty Queue";

        const item = this.elements.get(this.head);
        this.elements.delete(this.head);
        this.head++;
        return item;
    }

    peek() {
        return this.elements.get(this.head) || -1;
    }

    get length() {
        return this.tail - this.head;
    }

    get isEmpty() {
        return this.length === 0;
    }
}

export default Queue;
