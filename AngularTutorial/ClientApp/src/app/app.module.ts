import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { CoursesComponent } from './courses.component';
import { CourseComponent } from './course/course.component';
import { CoursesService } from './courses.service';

@NgModule({
  declarations: [
        AppComponent,
        CoursesComponent,
        CourseComponent
  ],
  imports: [
    BrowserModule
  ],
    providers: [
        // this is a singlton that needs to be added in to show dependencies
        // will pass a single instance to all the components within CoursesService
        CoursesService
    ],
  bootstrap: [AppComponent]
})
export class AppModule { }
