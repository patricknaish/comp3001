TemplateBook = {
    Run: function(){
        if( ($("#template_isbn").val() == "-1") && ($("#link_section").css("display") == "none") )
            $("#link_section").slideToggle(500);
        if( ($("#template_isbn").val() != "-1") && ($("#link_section").css("display") != "none") ) 
            $("#link_section").slideToggle(500);
        TemplateBook.Update($("#template_isbn").val());
    },

    Update: function(id){
        jQuery.ajax({
            url: "/json/book?isbn=" + id,
            dataType: "json",
            success: function(data, XHR, statusText){
                $("#json_isbn").html(data.isbn);
                $("#json_year").html(data.year);
                $("#json_edition").html(data.edition);
                $("#json_publisher").html(data.publisher);
                $("#json_rrp").html(data.rrp / 100);
                $("#json_author").html(data.author);
            }
        });
    }
}
