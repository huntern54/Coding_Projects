// when using "interfaces", always use Pascal naming conventions
// this point is a class
export class Point {

    constructor(private _x?: number, private _y?: number) { }

    // function that is part of a class is called a 'Meta'
    draw() {
        console.log('X: ' + this._x + ', Y: ' + this._y);
    }

    /*    // getter
        get x() {
            return this._x;
        }
    
        // setter
        set x(value) {
            if (value < 0)
                throw new Error('value cannot be less than 0');
    
            this._x = value;
        }*/
}
