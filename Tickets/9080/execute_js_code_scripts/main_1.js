function checkMascota(mascota){
  switch (mascota) {
    case "lagarto":
      text = "Tengo un lagarto";
      break;
    case "perro":
      text ="Tengo un perro";
      break;
    case "gato":
      text = "Tengo un gato";
    break;
    case "serpiente":
      text ="Tengo una serpiente";
      break;
    case "loro":
      text = "Tengo un loro";
      break;
    default:
      text = "Mascota no esta en la lista";
      break;
  }
  return text;
}

checkMascota(user_input);