import { Component, OnInit } from '@angular/core';
import { Post } from '../post';
import { PostService } from '../post.service';

import * as $ from 'jquery';
declare var $: any;
@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {

  constructor(private postService: PostService) { }

  ngOnInit() {
    this.getPost();
  }

  posts:Post[];

  getPost(){
    this.postService.getPosts().subscribe(posts => this.posts = posts);
  }

  add(title:string, body:string):void {
    let newPost = new Post;
    newPost.title = title;
    newPost.body = body;
    this.postService.addPost(newPost).subscribe(post => this.posts.push(post));
  }
}
 