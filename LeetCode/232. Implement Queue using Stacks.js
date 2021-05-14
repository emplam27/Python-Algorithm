/**
 * Initialize your data structure here.
 */
var MyQueue = function () {
  this.stack1 = [];
  this.stack2 = [];
};

/**
 * Push element x to the back of queue.
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function (x) {
  this.stack1.push(x);
};

/**
 * Removes the element from in front of queue and returns that element.
 * @return {number}
 */
MyQueue.prototype.pop = function () {
  // stack2에 요소가 남아있지 않다면, stack1에 있는 요소들을 모두 stack2로 옮긴 후 pop
  // stack2에 요소가 남아있다면, 그냥 pop
  if (this.stack2.length === 0) {
    if (this.stack1.length === 0) return -1;
    while (this.stack1.length !== 0) {
      this.stack2.push(this.stack1.pop());
    }
  }
  return this.stack2.pop();
};

/**
 * Get the front element.
 * @return {number}
 */
MyQueue.prototype.peek = function () {
  if (this.stack2.length === 0) {
    return this.stack1[0];
  }
  return this.stack2[this.stack2.length - 1];
};

/**
 * Returns whether the queue is empty.
 * @return {boolean}
 */
MyQueue.prototype.empty = function () {
  if (this.stack1.length === 0 && this.stack2.length === 0) {
    return true;
  }
  return false;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
