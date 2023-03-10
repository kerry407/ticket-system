import styles from './login.module.css'

const login = () => {
  return (
    <div className={styles.login}>
        <h1>Get-Ticketz</h1>
        <form action="">
            <h2>Login</h2>
        
        <label htmlFor="">Email or Phone Number</label> <br />
        <input type="text" placeholder='Enter email address or phone number' />

        <label htmlFor="">Email or Phone Number</label> <br />
        <input type="password" placeholder='Enter your password' />
        <div><button>Forgot password?</button></div>
        <button className={styles.submitButton}>Login</button>
        </form>
    </div>
  )
}

export default login