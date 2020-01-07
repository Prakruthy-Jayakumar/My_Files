import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PostsComponent } from '../post/posts/posts.component';
import { PostDetailsComponent } from '../post/post-details/post-details.component';
import { EditPostComponent } from './edit-post/edit-post.component';
import { CreatePostComponent } from './create-post/create-post.component';

const routes: Routes = [
	{path:'', component:PostsComponent},
  {path: ':id/view', component: PostDetailsComponent },
  {path: ':id/edit', component: EditPostComponent },
  {path: '/create', component: CreatePostComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PostRoutingModule { }




