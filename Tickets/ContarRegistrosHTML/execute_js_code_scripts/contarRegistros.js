function contarRegistros(){
    var rowCount_ = document.getElementById("example").rows.length;
    //Dado que la tabla tiene thead y tfoot debemos descontar 2 al total de registros
    rowCount_ = rowCount_-2;
    return rowCount_;
}
contarRegistros();