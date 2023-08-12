import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-tweet',
  templateUrl: './tweet.component.html',
  styleUrls: ['./tweet.component.css']
})
export class TweetComponent {
  tweets: string[] = [];
  newTweet: string = '';

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.getTweets();
  }

  getTweets() {
    this.http.get<string[]>('http://localhost:3000/tweets').subscribe(data => {
      this.tweets = data;
    });
  }

  onSubmit() {
    if (this.newTweet) {
      this.http.post<any>('http://localhost:3000/tweets', { tweet: this.newTweet }).subscribe(() => {
        this.newTweet = '';
        this.getTweets();
      });
    }
  }
}
