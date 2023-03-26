import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  return Promise.all([...promises])
    .then((values) => {
      const dataBody = values[0].body;
      const name = `${values[1].firstName} ${values[1].lastName}`;
      console.log(`${dataBody} ${name}`);
    })
    .catch(console.log('Signup system offline'));
}
