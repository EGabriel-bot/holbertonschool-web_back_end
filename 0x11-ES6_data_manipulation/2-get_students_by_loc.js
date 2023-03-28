export default function getStudentsByLocation(listOfStudents, city) {
  return listOfStudents.filter((object) => object.location === city);
}
