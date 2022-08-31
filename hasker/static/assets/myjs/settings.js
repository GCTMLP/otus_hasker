let app = new Vue({
  el: "#settings",
  delimiters: ["{", "}"],
  data: {
    login: null,
    foto: null,
    file: null,
    email: null,
    request: false,
    visible: true,
    settings: {},
    styleObject: {
      width: '118px',
      height: '118px',
      background: this.foto,
    },
  },

  methods: {
    init: function() {
        this.get_settings();
    },
    get_settings: function() {
      axios.post("get_settings/", {
        'Accept': 'application/json'
        
      }).then(async response => {
        const data = await response.data;
        all_data = JSON.parse(data)
        this.login = all_data['login']
        this.email = all_data['email']
        this.foto = all_data['foto']
      });
    },

    submitFile(){
            let formData = new FormData();
            formData.append('file', this.file);
            formData.append('login', this.login);
            formData.append('email', this.email);
            axios.post( 'change_user_data/',
                formData
            ).then(async response => {
            const data = await response.data;
            if (data == 'true'){
              this.$toastr.defaultTimeout = 3000;
              this.$toastr.defaultPosition = "toast-top-right";
              this.$toastr.defaultStyle = { "background-color": "green" },
              this.$toastr.s("You changed data");
              app1.get_user_data()
            }
            else{
              this.$toastr.defaultTimeout = 3000;
              this.$toastr.defaultPosition = "toast-top-right";
              this.$toastr.defaultStyle = { "background-color": "red" },
              this.$toastr.s("Errors in changed data");
            }
            
        })
    },
    hide_foto(){
      this.visible = false
      this.file = this.$refs.file.files[0];
    },
      

  },
  mounted: function () {
  this.init();
  }
    
})
