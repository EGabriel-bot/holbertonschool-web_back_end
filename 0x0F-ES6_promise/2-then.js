export default function handleResponseFromAPI(promise) {
  promise.then(
    () => {
      const resolve = { status: 200, body: 'success' };
      console.log('Got a response from the api');
      return resolve;
    },
    (reject) => reject(new Error()),
  );
}
