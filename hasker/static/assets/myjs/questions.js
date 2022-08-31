let app = new Vue({
  
  el: "#questions",
  delimiters: ["{", "}"],
  data: {
    request: false,
    questions: {},
    istag_invalid: false,
    popular_questions: {},
    filter: {
      page: 1,
      limit: 5,
      pages_big: 0,
      search: '',
    },
    new_quest: {
      title: null,
      text: null,
      tags: null,
    }
  },
  methods: { 
    init: function() {
        this.get_questions(this.filter.page);
        this.get_popular_questions()   

    },
    get_questions: function(page) {
      const params = {
        page: page,
        limit: this.filter.limit,
        search: this.filter.search
      };
      axios.post("get_all_questions/", params, {
        'Accept': 'application/json'
        
      }).then(async response => {
        const data = await response.data;
        all_data = JSON.parse(data)
        
        this.questions = all_data['data']
        q_count = Number(all_data['count'])
        this.filter.pages = Math.floor(q_count / this.filter.limit);
        if(q_count % this.filter.limit != 0){
          this.filter.pages += 1
        }
      });

    },

    get_popular_questions: function(page) {
      
      axios.post("get_popular_questions/",{
        'Accept': 'application/json'
        
      }).then(async response => {
        const data = await response.data;
        all_data = JSON.parse(data)
        this.popular_questions = all_data
      });
      
    },
    // get_vote_questions: function(page) {
    //   axios.post("get_vote_questions/", {
    //     'Accept': 'application/json'
        
    //   }).then(async response => {
    //     const data = await response.data;
    //     all_data = JSON.parse(data)
        
    //   });
    // },
    minus_page: function(){
      if (this.filter.page % 5 == 0 && this.filter.pages_big+1 == this.filter.page){
        this.filter.pages_big-=4
        this.filter.page = this.filter.page-=1
      }
      else{
        this.filter.page = this.filter.page-=1
      }
      if(this.filter.page % 5 == 0 ){
        this.filter.pages_big-=4
      }
      this.get_questions(this.filter.page)
    },

    plus_page: function(){
      if (this.filter.page % 5 == 0 && this.filter.pages_big+5 == this.filter.page){
        this.filter.pages_big+=4
        this.filter.page = this.filter.page+=1
      }
      else{
        this.filter.page = this.filter.page+=1
      }
      if(this.filter.page % 5 == 0){
        this.filter.pages_big+=4
      }
      this.get_questions(this.filter.page)
    },

    change_page_big: function(page_chosen){
      if(page_chosen % 5 == 0 && page_chosen > this.filter.page){
        this.filter.pages_big+=4
      }
      if(page_chosen % 5 == 0 && page_chosen < this.filter.page){
        this.filter.pages_big-=4
      }
      this.filter.page = page_chosen
      this.get_questions(this.filter.page)
    },
    change_count: function(limit){
      this.filter.limit = limit
      this.filter.page = 1
      this.get_questions(this.filter.page);
    },
    clean_search: function(){
      this.filter.search = null
      this.get_questions(1)
    },

    search_tag: function(tag){
      this.filter.search = '#'+tag
      this.get_questions(1)
    },

    ask_question: function(){
      try{
        if (this.new_quest.tags.split('; ').length <=3){
          params = {
            title: this.new_quest.title,
            text: this.new_quest.text,
            tags: this.new_quest.tags,
          }

          axios.post("ask_question/", params, {
            'Accept': 'application/json'
            
          }).then(async response => {
            const data = await response.data;
            if (data != 'false'){
              
              window.location.href = '/answers?q='+data
            }
            else {
              this.$toastr.defaultTimeout = 3000;
              this.$toastr.defaultPosition = "toast-top-right";
              this.$toastr.defaultStyle = { "background-color": "red" },
              // Send message to browser screen
              this.$toastr.s(
                "Some errors in your question"
              );
            }
            
          });

        }
        else {
          this.istag_invalid = true

        }
      }
      catch{
      this.$toastr.defaultTimeout = 3000;
            this.$toastr.defaultPosition = "toast-top-right";
            this.$toastr.defaultStyle = { "background-color": "red" },
            // Send message to browser screen
            this.$toastr.s(
              "Some errors in your question"
            );
      }
    },

    plus_vote: function(id){
      params={
        id: id
      }
      axios.post("plus_vote/", params, {
        'Accept': 'application/json'
          
      }).then(async response => {
        this.init()      
      });
    },
    minus_vote: function(id){
      params={
        id: id
      }
      axios.post("minus_vote/", params, {
        'Accept': 'application/json'
          
      }).then(async response => {
        this.init()           
      });
    }

  },
  mounted: function () {
  this.init();
  }
})

