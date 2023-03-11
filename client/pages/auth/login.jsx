import styles from './login.module.css'
import Link from 'next/link'

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

        <div className={styles.account}>
            Don't have an account?
            <div>
                <Link  href={`/auth/signup`}>
                <button type="button">Create account</button>
                </Link>
            </div>
        </div>
        </form>
    </div>
  )
}

export default login