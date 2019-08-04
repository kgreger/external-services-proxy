# myModel.R

#' Make R write a message
#' @param message The message to echo back.
#' @post /r_says_hello
#' @serializer unboxedJSON
function(message="Hello!"){
  return(list(result = paste0("R and says: ", message)))
}
