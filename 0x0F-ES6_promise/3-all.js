import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  return Promise.all([...promises])
    .then((values) => {
      const { body } = values[0];
      const { firstName } = values[1];
      const { lastName } = values[1];

      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(console.log('Signup system offline'));
}
