import Card from '../Card/Card'
import styles from './Intro.module.css'

const Intro = () => {
  return (
    <div className={styles.intro}>
      <div className={styles.features}>
        <div>
          <i className="fa-solid fa-circle-check"></i>
          <h2>Choose Events and Tickets</h2>
          <span>with only a few clicks</span>
        </div>

        <div>
        <i className="fa-solid fa-cart-shopping"></i>
          <h2>Buy directly from organizers</h2>
          <span>Pay online in easy steps</span>
        </div>

        <div>
        <i className="fa-solid fa-ticket"></i>
          <h2>Get ticketz!</h2>
          <span>Sent to your email</span>
        </div>
      </div>
      <div className={styles.heading}>
      <h2>Popular Events in <span>Abuja</span></h2>
      <h3>Filter by Category</h3>
      </div>


        <div className={styles.events}>
            {
                [...Array(6)].map((x,i) =>  ( 
                    <Card key={i} />
                ))
            }
        </div>
    </div>
  )
}

export default Intro