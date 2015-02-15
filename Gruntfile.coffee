module.exports = (grunt) ->

  dist_directory = "dist"

  vendorfiles = {
    fonts: [
      'components/font-awesome/font/FontAwesome.otf'
      'components/font-awesome/font/fontawesome-webfont.eot'
      'components/font-awesome/font/fontawesome-webfont.svg'
      'components/font-awesome/font/fontawesome-webfont.ttf'
      'components/font-awesome/font/fontawesome-webfont.woff'
    ]
    js: [
      "components/jquery/jquery.min.js"
      "components/bootstrap/js/bootstrap-transition.js"
      "components/bootstrap/js/bootstrap-alert.js"
      "components/bootstrap/js/bootstrap-modal.js"
      "components/bootstrap/js/bootstrap-dropdown.js"
      "components/bootstrap/js/bootstrap-scrollspy.js"
      "components/bootstrap/js/bootstrap-tab.js"
      "components/bootstrap/js/bootstrap-tooltip.js"
      "components/bootstrap/js/bootstrap-popover.js"
      "components/bootstrap/js/bootstrap-button.js"
      "components/bootstrap/js/bootstrap-collapse.js"
      "components/bootstrap/js/bootstrap-carousel.js"
      "components/bootstrap/js/bootstrap-typeahead.js"
    ]
  }

  grunt.loadNpmTasks('grunt-contrib-watch')
  grunt.loadNpmTasks('grunt-contrib-less')
  grunt.loadNpmTasks('grunt-contrib-copy')
  grunt.loadNpmTasks('grunt-contrib-clean')
  
  # Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json')
    delta:
      less:
        tasks: 'less'
        files: ['less/*.less', 'less/**/*.less']

    less:
      all:
        options:
          paths: ["less", "components"]
        files:
          "css/styles.css": "less/styles.less"

    copy:
      vendor:
        files: [{
          expand: true
          flatten: true
          src: vendorfiles.fonts
          dest: "#{dist_directory}/vendor/fonts/"
        }, {
          expand: true
          flatten: true
          src: vendorfiles.js
          dest: "#{dist_directory}/vendor/js/"
        }]

    clean:
      dist: ['dist']
  })

  grunt.registerTask('build', [
    'less:all'
    'copy:vendor'
  ])

  # Rename the watch task to delta, and make a new watch task that runs
  # build on startup
  grunt.renameTask('watch', 'delta')
  grunt.registerTask('watch', [
    'build'
    'delta'
  ])

  grunt.registerTask('default', ['build'])

