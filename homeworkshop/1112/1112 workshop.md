# 1112 workshop

- kakao oven (https://ovenapp.io/)
- https://balsamiq.com/
- figma(https://www.figma.com/)

---

### App

- searchBar
- videoList
  - videoListItem
  - videoListItem
  - videoListItem



---



### 1.컴포넌트부터제작 

### 2. SearchBar.vue

- https://developers.google.com/youtube/v3/docs?hl=ko (유튜브 api 참조)

- https://developers.google.com/youtube/v3/docs/search/list?hl=ko (search list)

- https://joshua1988.github.io/vue-camp/deploy/env-setup.html#vue-cli-3-x-%EB%B2%84%EC%A0%84%EC%9D%98-%ED%99%98%EA%B2%BD-%EB%B3%80%EC%88%98-%ED%8C%8C%EC%9D%BC-%EC%A0%91%EA%B7%BC (vue 환경변수 )

  ```
  //.env.local
  VUE_APP_YOUTUBE_API_KEY=AIzaSyCk52y-NA-4W_DOohpl_M56NLv-f1aqQUs
  ```

  ```html
  <script>
  import axios from 'axios'
  const BASE_URL = 'https://www.googleapis.com/youtube/v3/search'
  const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
  export default {
  	name: 'SearchBar',
  	data(){
  		return{
  			userInput:'',
  		}
  	},
  	methods:{
  		fetchVideos(e){
  			this.userInput = e.target.value
  			const config = {
  				params: { // axios의 params
  					part:'snippet',
  					key : API_KEY,
  					q:this.userInput
  				}
  			}
  			// 필수 매개변수 확인 -> id or snippet
  			axios.get(BASE_URL, config)
  			.then(res=>{
  				console.log(res)
  			})
  			.catch(err=>{
  				console.log(err)
  			})
  		}
  	}
  }
  </script>
  ```




- ETag : 고유값

---

### 3. VideoList

- XSS -> 공격 방지 : 데이터 보호 (**#39;Dynamite&#39 **... 이런식으로 처리)
  - `직접 parsing` or 라이브러리(lodash -> unescape)
  - vue -> filters 

```vue
	<p class = "videoListItem_title">{{video.snippet.title | unescape}}</p>

	fitlers:{
		unescape: function (raw) {
      return _.unescape(raw)
    }
},
```

**VideoList** > template

```vue
<template>
	<div class = "videoList">
		<VideoListItem
		v-for="video in videoList" :key="video.etag"
		:video='video'
	
		@select-videos='selectVideo'
		/>
		<!-- <img width=360 :src="thumbnailUrl(video)" alt="">
			<div>

			<p class = "videoListItem_title">{{video.snippet.title | unescape}}</p>
			<p class = "videoListItem_channelTitle">{{video.snippet.channelTitle}}</p>
			<p class = "videoListItem_description">{{video.snippet.description}}</p>
			</div>  -->
	</div>

</template>
```

**script**

```vue
<script>
import VideoListItem from '@/components/VideoListItem.vue'
// import _ from 'lodash'

export default {
	name : 'VideoList',
	components:{
		VideoListItem,
	},
	props:{
		videoList : Array, 
	},
	// fitlers:{
	// 	unescape: function (raw) {
  //     return _.unescape(raw)
  //   }
	// },
	methods:{
	selectVideo(video){
		console.log(video)
		this.$emit('select-videos',video)
	}
	// 	// 
	// 	thumbnailUrl(video){
	// 		return video.snippet.thumbnails.high.url
	// 	}
	}
}
</script>
```

---

### 4. VideoListItem

```vue
<template>
	<div @click ="onSelectVideo" 	class = "videoListItem">
		<img width=360 :src="thumbnailUrl(video)" alt="">
			<div>
			<p class = "videoListItem_title">{{video.snippet.title | unescape}}</p>
			<p class = "videoListItem_channelTitle">{{video.snippet.channelTitle}}</p>
			<p class = "videoListItem_description">{{video.snippet.description}}</p>
			
			</div>

	</div>
</template>

<script>
import _ from 'lodash'
export default {
	name: 'VideoListItem',
	props:{
		video:Object,
	},
	filters:{
		unescape: function (raw) {
      return _.unescape(raw)
    }
	},
	methods:{
		// 
		thumbnailUrl(video){
			return video.snippet.thumbnails.high.url
		},
		onSelectVideo(){
			this.$emit('select-videos', this.video)
		}
	}
}
</script>

<style scoped>
/* scoped로 고립 */
.videoListItem{
	display: flex;
}
.videoListItem_title{
	font-size : 1.25rem; 
	/* 1rem =16px */
	font-weight: bold;
}
</style>
```





---

### 추가

**<네트리파이>**

1. `new site from git`

   - 환경변수 : site settings > build & deploy > Environment 

   - ## [Continuous Deployment]

     -  깃헙을 갱신하면 자동 배포

**<젠킨스>**

​	1. 공부해볼것..