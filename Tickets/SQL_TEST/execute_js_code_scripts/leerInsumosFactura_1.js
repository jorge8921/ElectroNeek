contenidoArchivoExcelFacturas=contenidoArchivoExcelFacturas.map(e=>{return {
AC:e["AC"]==undefined ? "" : e["AC"],
numeroCesion:e["# Cesion Titularidad"]==undefined? "" :e["# Cesion Titularidad"],
facturaSRI:e["Factura SRI"]==undefined?"":e["Factura SRI"],
fechaFactura:e["FechaFact."]==undefined?"":e["FechaFact."],
cliente:e["Cliente:"]==undefined?"":e["Cliente:"],
textoBreveMaterial:e["Texto breve de material"]==undefined?"":e["Texto breve de material"],
cdtaFacturada:e["Ctd.fact."]==undefined?"":e["Ctd.fact."],
notaCreditoDevolucion:e["N/C Devol."]==undefined?"":e["N/C Devol."],
fechaNotaCredito:e["Fecha  NC "]==undefined?"":e["Fecha  NC "],
codigoInscrLkBco:e["C. INS-Lk BCO"]==undefined?"":e["C. INS-Lk BCO"],
partidaArancelaria:e["P. Aranc."]==undefined?"":e["P. Aranc."],
descripcionItem:e["DESCRIP."]==undefined?"":e["DESCRIP."],
tipoUnidad:e["TIPO UND"]==undefined?"":e["TIPO UND"],
maxCnLiBco:e["Máx. de CN LI BCO"]==undefined?"":e["Máx. de CN LI BCO"],
maxCdLiBco:e["Máx. de CD LI BCO"]==undefined?"":e["Máx. de CD LI BCO"]
}});