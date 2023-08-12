import { CoursesService } from './courses.service'
import { Component } from '@angular/core'

@Component({
    selector: 'courses',

    /*        // example of string interpolation
    template: '<h2>{{ getTitle() }}</h2>'*/

    template: `
        <h2>{{ title }}</h2>
        <ul>
            <li *ngFor="let course of courses">
                {{ course }}
            </li>
        </ul>
    `

})
export class CoursesComponent {
    title = "List of courses";
    courses: string [] = [];

    // where we initalize an obj
    // now we show that the constructor has a dependency of type 'CourseService'
    // good for unit testing as well 
    constructor(service: CoursesService) {
    /*
        // not necessary since this could get fragile is if we start to add params
        let service = new CoursesService();
    */        

        this.courses = service.getCourses();
    }

    //logic needed to call an HTTP serivce

/*
    getTitle() {
        return this.title
    }*/
}
