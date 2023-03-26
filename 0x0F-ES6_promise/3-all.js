import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  return Promise.all([...promises])
    .then((values) => {
      const { body } = values[0];
      const name = `${values[1].firstName} ${values[1].lastName}`;

      console.log(`${body} ${name}`);
    })
    .catch(() => console.log('Signup system offline'));
}
